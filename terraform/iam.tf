resource "google_service_account" "cf_notification" {
  account_id = "cf-notification-${random_string.suffix.id}"
}

resource "google_service_account" "cf_notification_process" {
  account_id = "cf-notification-process-${random_string.suffix.id}"
}

resource "google_service_account" "workflow" {
  account_id = "wf-${random_string.suffix.id}"
}

resource "google_service_account" "apigw" {
  account_id = "apigw-${random_string.suffix.id}"
}

# TODO: Allow access to the VertexAI endpoint
# resource "google_project_iam_member" "project_viewer" {
#   for_each = toset(var.project_viewer)

#   member  = "serviceAccount:${google_service_account.cf_notification_process.email}"
#   project = each.value
#   role    = "roles/browser"
# }
